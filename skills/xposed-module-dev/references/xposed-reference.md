# Xposed/LSPosed Reference Notes

Use these notes as a local reference. If exact API versions, dependency coordinates, LSPosed release status, or Android compatibility matter, verify against the upstream docs because LSPosed/libxposed has changed over time.

## Modern libxposed API

Primary sources:

- libxposed API package docs: https://libxposed.github.io/api/io/github/libxposed/api/package-summary.html
- LSPosed modern API wiki: https://github.com/LSPosed/LSPosed/wiki/Develop-Xposed-Modules-Using-Modern-Xposed-API
- Example module: https://github.com/libxposed/example

Important points:

- Modern modules use `io.github.libxposed.api`.
- Entry classes extend `XposedModule`.
- Java entries are registered in `META-INF/xposed/java_init.list`.
- Native entries are registered in `META-INF/xposed/native_init.list`.
- These files should be placed under `src/main/resources/META-INF/xposed/` so Gradle packages them into the APK.
- Module name and description come from normal Android resources: `android:label` and `android:description`.
- Module configuration is `META-INF/xposed/module.prop`, formatted as Java properties.
- Required modern properties include `minApiVersion` and `targetApiVersion`.
- The current official example uses API version `101` in both `module.prop` and Gradle dependency versions. Verify the latest API version before creating a new template.
- `staticScope` is optional and tells the manager whether the listed scope is fixed.
- Scope is `META-INF/xposed/scope.list`, one package name per line.
- Modern API dependency should be `compileOnly("io.github.libxposed:api:<version>")` because the framework supplies the runtime implementation.
- With Android Gradle Plugin, ensure `META-INF/xposed/*` remains packaged. The official example merges this pattern under `packaging.resources`.
- Modern modules should filter callbacks by package and process because injected processes can produce callbacks beyond the originally scoped package.
- Use `system` as the virtual package name for `system_server` scope.
- `android` is not the same as `system`; some Android package components can still load outside system_server.
- Hooking uses `hook(Executable)` and an interceptor chain. Call `chain.proceed()` to run the next hook/original path.
- `onModuleLoaded()` runs once when the module is loaded in a target process.
- `onPackageLoaded()` runs when the default classloader is ready, before `AppComponentFactory` on Android 10+.
- `onPackageReady()` runs after the app classloader is ready.
- `onSystemServerStarting()` runs when system_server starts.
- Resource hooks from legacy API are not supported by the modern API.
- The LSPosed wiki warns the modern API was still not fully stable in its 2023-era documentation; verify before promising stable release compatibility.

## Legacy XposedBridge API

Primary sources:

- `IXposedHookLoadPackage`: https://api.xposed.info/reference/de/robv/android/xposed/IXposedHookLoadPackage.html
- `XposedHelpers`: https://api.xposed.info/reference/de/robv/android/xposed/XposedHelpers.html
- API overview: https://api.xposed.info/reference/packages.html

Important points:

- Legacy modules use package `de.robv.android.xposed`.
- App-load hooks implement `IXposedHookLoadPackage`.
- The framework calls `handleLoadPackage(XC_LoadPackage.LoadPackageParam lpparam)` very early when an app package is loaded.
- Common helper APIs include `XposedHelpers.findAndHookMethod`, `findAndHookConstructor`, `findClass`, `findClassIfExists`, `findMethodExact`, field getters/setters, and `XC_MethodHook`.
- Legacy entry classes are normally registered in `assets/xposed_init`.
- Legacy module metadata is normally stored in AndroidManifest `<meta-data>` entries such as `xposedmodule`, `xposeddescription`, and `xposedminversion`.
- The Xposed API dependency should be `compileOnly` because the framework provides it at runtime.

## Practical Compatibility Guidance

- Choose modern libxposed when building primarily for current LSPosed and when the project can accept modern API constraints.
- Choose legacy XposedBridge for older modules, ports, broad compatibility with existing examples, or when resource hooks are required.
- Do not package framework implementation classes into the module APK.
- Do not use reflection to call modern Xposed APIs; modern API call protection is enforced.
- Prefer exact method signatures for hooks. If an obfuscated app changes signatures, fail with useful logging instead of crashing.
