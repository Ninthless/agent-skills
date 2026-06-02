---
name: xposed-module-dev
description: 'Use for Android Xposed, LSPosed, libxposed, XposedBridge, hook development, module skeletons, module activation, scope.list, module.prop, xposed_init, IXposedHookLoadPackage, XposedHelpers, XC_MethodHook, migration from legacy to modern API, LSPosed not showing modules, logcat debugging, 写 Xposed 模块, LSPosed 模块, hook 安卓 App, 模块不显示, and Android hook review.'
when_to_use: 'Use when the user wants to build, review, migrate, or debug Android Xposed or LSPosed modules. Also use for libxposed, legacy XposedBridge, hook code, module activation failures, scope or metadata files, and logcat troubleshooting.'
---

# Xposed Module Development

## Triggers

- The user wants to build, review, migrate, or debug an Android Xposed or LSPosed module.
- The task mentions libxposed, XposedBridge, hooks, scope.list, module.prop, xposed_init, or logcat.
- The user needs help with module activation, module not showing in LSPosed, scope problems, or metadata files.
- The user asks to migrate from legacy XposedBridge to modern libxposed.
- The user says `写 Xposed 模块`, `LSPosed 模块`, `hook 安卓 App`, `模块不显示`, `作用域`, or `迁移到 libxposed`.

Use this skill to help users develop correct Android Xposed/LSPosed modules. Prefer current LSPosed/libxposed patterns for new modules, but recognize and support legacy XposedBridge projects when the repository already uses them or the user explicitly targets old API compatibility.

## First Decision

Before writing code, identify which API family the project uses:

- **Modern libxposed API**: entry class extends `io.github.libxposed.api.XposedModule`; registration lives under `src/main/resources/META-INF/xposed/`; hook code uses `hook(Executable)` and interceptor chains.
- **Legacy XposedBridge API**: entry class implements `IXposedHookLoadPackage`, `IXposedHookZygoteInit`, or resource hook interfaces; registration is usually `src/main/assets/xposed_init`; hook code uses `XposedHelpers.findAndHookMethod`, `XC_MethodHook`, or `XC_MethodReplacement`.

Do not mix modern `io.github.libxposed.api` with legacy `de.robv.android.xposed` in the same module unless the user has a very specific compatibility plan. The two systems have different entry registration, lifecycle, metadata, and hook APIs.

## Modern Module Checklist

For a new LSPosed module, produce or verify this structure:

```text
app/src/main/AndroidManifest.xml
app/src/main/java/<package>/<Entry>.java
app/src/main/resources/META-INF/xposed/java_init.list
app/src/main/resources/META-INF/xposed/module.prop
app/src/main/resources/META-INF/xposed/scope.list
```

Use Android resources for the module name and description:

```xml
<application
    android:label="@string/app_name"
    android:description="@string/module_description">
</application>
```

Use `module.prop` for framework API requirements:

```properties
minApiVersion=101
targetApiVersion=101
staticScope=true
```

Declare the modern Xposed API dependency as `compileOnly`; it is provided by the framework at runtime. If the Android Gradle plugin strips Java resources, configure packaging so `META-INF/xposed/*` stays in the APK. In Kotlin DSL projects, the official example uses this shape:

```kotlin
packaging {
    resources {
        merges += "META-INF/xposed/*"
        excludes += "**"
    }
}

dependencies {
    compileOnly("io.github.libxposed:api:<version>")
}
```

Use `java_init.list` with one fully qualified entry class per line:

```text
com.example.module.MainHook
```

Use `scope.list` with one target package per line:

```text
com.target.app
system
```

For system hooks, use `system` when the code runs inside `system_server`. Keep `android` only for Android package components that actually load outside system_server.

## Modern Entry Pattern

Use this shape as the baseline. Adjust names and target classes to the user's project.

```java
package com.example.module;

import android.util.Log;
import io.github.libxposed.api.XposedModule;

import java.lang.reflect.Method;

public final class MainHook extends XposedModule {
    private static final String TAG = "ExampleModule";

    @Override
    public void onPackageReady(PackageReadyParam param) {
        if (!"com.target.app".equals(param.getPackageName())) {
            return;
        }

        try {
            Class<?> clazz = param.getClassLoader().loadClass("com.target.app.TargetClass");
            Method method = clazz.getDeclaredMethod("targetMethod", String.class);
            hook(method).intercept(chain -> {
                Object arg = chain.getArg(0);
                Log.i(TAG, "targetMethod arg=" + arg);
                Object result = chain.proceed();
                return result;
            });
        } catch (ReflectiveOperationException e) {
            Log.e(TAG, "Failed to install hook", e);
        }
    }
}
```

Prefer `onPackageReady()` for app hooks because the app classloader is ready. Use `onPackageLoaded()` only when the hook must happen before `AppComponentFactory` or very early app initialization. Use `onSystemServerStarting()` for system server hooks.

## Legacy Module Checklist

For existing legacy projects, verify:

```text
app/src/main/assets/xposed_init
app/src/main/AndroidManifest.xml
app/build.gradle(.kts)
```

Legacy `xposed_init` contains one fully qualified entry class per line:

```text
com.example.module.MainHook
```

Legacy metadata is normally declared on the application element:

```xml
<meta-data android:name="xposedmodule" android:value="true" />
<meta-data android:name="xposeddescription" android:value="@string/module_description" />
<meta-data android:name="xposedminversion" android:value="93" />
```

Declare the Xposed API dependency as `compileOnly`; it is provided by the framework at runtime and should not be packaged into the APK.

## Legacy Entry Pattern

```java
package com.example.module;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage;

public final class MainHook implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam lpparam) throws Throwable {
        if (!"com.target.app".equals(lpparam.packageName)) {
            return;
        }

        XposedHelpers.findAndHookMethod(
            "com.target.app.TargetClass",
            lpparam.classLoader,
            "targetMethod",
            String.class,
            new XC_MethodHook() {
                @Override
                protected void beforeHookedMethod(MethodHookParam param) {
                    String value = (String) param.args[0];
                }
            }
        );
    }
}
```

## Hooking Rules

- Filter by `packageName` and, when relevant, `processName`. Modules can be injected into processes where multiple packages are observed.
- Use the target app's classloader, not the module app's classloader, for target classes.
- Hook the narrowest stable method you can identify. Avoid broad hooks such as `Application.attach()` as the final behavior unless it is only used to obtain context or classloader.
- Avoid doing heavy work in early callbacks. Install hooks quickly and defer I/O, networking, or long analysis.
- Catch reflection lookup failures around optional targets so one missing class does not crash the target process.
- Log the package, process, and hook installation result. Ask the user for `adb logcat` around the target process when debugging crashes.
- Treat obfuscated apps as moving targets. Prefer finding classes by stable behavior, signatures, resources, or call chains, and document the app version used for analysis.
- Do not hook banking, payment, DRM, anti-cheat, or third-party security controls for bypass or unauthorized access. Keep work scoped to legitimate debugging, customization, research on owned devices, or user-controlled apps.

## Common Failure Modes

- Module not appearing in LSPosed: missing registration file, wrong resources path, malformed `module.prop`, or APK installed for another Android user.
- Module appears but hook never runs: target package missing from scope, no reboot/restart after enabling, wrong process, or package name mismatch.
- Class not found: using the wrong classloader, hooking too early, dynamic feature not loaded, app obfuscation changed, or target code is native.
- Target app crashes: uncaught exception in callback, bad cast, wrong parameter list, returning an invalid replacement value, or triggering recursion by calling a hooked method incorrectly.
- Modern module ignored: old `assets/xposed_init` used instead of `META-INF/xposed/java_init.list`, or modern API called by reflection.
- Legacy module broken after migration: metadata, entry registration, resource hooks, and helper APIs were not translated to modern equivalents.

## Development Workflow

1. Inspect the repository before changing files. Determine Gradle DSL, Kotlin vs Java, AGP version, namespace, minSdk, and whether it already uses modern or legacy Xposed APIs.
2. Identify the target package, target process, Android/LSPosed version, and expected behavior change.
3. Add the smallest valid module skeleton for the selected API family.
4. Write hook code with explicit package/process filters and defensive reflection handling.
5. Build with Gradle. Fix compile errors before speculating about runtime behavior.
6. Install the APK, enable the module, set scope, force-stop or reboot as required, then inspect `adb logcat` filtered by module tag, LSPosed, and target package.
7. When debugging runtime failures, ask for or collect the exact stack trace and target app version. Do not guess from symptoms alone.

## When Explaining To Users

Respond in the user's language when practical. For Chinese users, explain the split clearly:

- 新项目默认建议现代 `libxposed` API。
- 旧项目或追求广泛兼容时继续用 `XposedBridge` legacy API。
- 两套 API 的入口文件、Manifest/metadata、scope 和 hook 写法不同，不能随意拼接。

If you provide code, include the files that must exist and where each snippet belongs. If the user only asks "怎么写", give a minimal working skeleton plus the build/install/enable/debug steps.

## References

Read `references/xposed-reference.md` when you need source-backed details about modern registration, lifecycle callbacks, scope behavior, or legacy API names.
