# Platform Guidelines

Read this reference for desktop software, native mobile apps, cross-platform shells such as Electron or Tauri, and web products that deliberately emulate a platform application.

## Contents

- Platform Fit
- Web
- Windows
- macOS
- iOS And iPadOS
- Android
- Cross-Platform Desktop
- Input And Windowing
- Platform Evidence
- Sources

## Platform Fit

Platform fit means users can transfer learned behavior into the product. It does not require visual imitation of first-party apps.

Preserve the product's identity while matching the host platform for:

- Window controls, title bars, menus, and system commands
- Navigation placement and back behavior
- Keyboard shortcuts and modifier keys
- Selection, context menus, drag and drop, and clipboard behavior
- Dialog modality, focus, confirmation, and cancellation
- File pickers, notifications, sharing, permissions, and system settings links
- Typography scaling, contrast modes, reduced motion, and assistive technology
- Pointer, touch, pen, gamepad, and keyboard expectations

When a product runs on multiple platforms, share product semantics and tokens but allow platform-specific interaction and chrome.

## Web

- Preserve browser behaviors for links, history, refresh, text selection, zoom, and native form controls.
- Use responsive composition based on available space and input, not device names alone.
- Avoid recreating native widgets when semantic HTML already supplies the interaction.
- Treat installable or desktop-like web apps as web first unless the product explicitly owns window and file-system behavior.
- Measure Core Web Vitals with field data when the surface has meaningful traffic; use lab measurements during implementation.

## Windows

- Follow Windows command, navigation, windowing, and keyboard conventions.
- Support standard shortcuts such as `Ctrl+C`, `Ctrl+V`, `Ctrl+Z`, `Ctrl+S`, `F1`, and `Alt+F4` when the corresponding actions exist.
- Use `Ctrl`-based accelerators and expose access keys where frequent keyboard operation matters.
- Place window controls in the expected caption area and do not create draggable regions over interactive content.
- Use native system dialogs or faithful platform behavior for files, permissions, notifications, and destructive confirmation.
- Respect text scaling, high contrast, Narrator, keyboard focus, and reduced animation settings.
- Keep dense productivity interfaces efficient; Fluent styling does not require turning every region into a spacious card.

## macOS

- Use the menu bar for application commands and standard menu organization when building a desktop app.
- Use `Command` for primary shortcuts and preserve common shortcuts such as `Command+Q`, `Command+W`, `Command+,`, `Command+S`, and `Command+Z` when applicable.
- Respect the standard placement and behavior of window controls, sheets, panels, inspectors, toolbars, and full-screen mode.
- Make close, minimize, quit, and document-save behavior consistent with document state.
- Use system pickers, share services, notifications, permissions, and preferences patterns when available.
- Support VoiceOver, Full Keyboard Access, increased contrast, reduced motion, and text-size expectations.

## iOS And iPadOS

- Preserve standard navigation-bar, tab-bar, back-swipe, modal, sheet, and keyboard behavior.
- Keep the primary action reachable without obscuring content or conflicting with the home indicator and safe areas.
- Use controls sized for touch and allow Dynamic Type without clipping or hiding actions.
- Support rotation, split view, pointer, keyboard, and multitasking on iPad when the product scope includes them.
- Request permissions in context and explain the user benefit before the system prompt when explanation is needed.
- Respect platform gestures; do not replace a familiar back or dismissal behavior without a strong task reason.

## Android

- Preserve system back behavior and predictive back where supported.
- Use navigation bars, rails, drawers, sheets, dialogs, snackbars, and system surfaces according to the product's information architecture rather than by habit.
- Support font scaling, TalkBack, contrast, reduced motion, touch targets, and edge-to-edge safe insets.
- Use platform permission and notification flows and handle denial without dead ends.
- Respect hardware and software keyboard behavior, including IME actions and focus movement in forms.

## Cross-Platform Desktop

Electron, Tauri, Qt, Flutter, and similar frameworks can cover desktop UI, but the design contract must name the target operating systems.

- Decide whether the app uses native window chrome, a custom title bar, or a hybrid per platform.
- Map shortcuts by platform instead of displaying `Ctrl` everywhere.
- Use platform-specific menu placement and application lifecycle behavior.
- Test resizing, maximize, full screen, multiple windows, multiple monitors, display scaling, and restored window bounds.
- Test file dialogs, drag and drop, clipboard, deep links, notifications, updates, offline behavior, and unsaved-work recovery when present.
- Keep canvas-heavy editors and creative tools focused on the artifact; panels, inspectors, timelines, and toolbars should support repeated expert work.
- Avoid a browser-page composition inside a desktop window when users expect a command-rich application.

## Input And Windowing

For desktop software, verify:

- Keyboard-only completion of the primary task
- Shortcut discoverability and conflicts
- Context menus and right-click behavior
- Drag threshold, drop feedback, cancellation, and non-drag alternatives
- Focus restoration across dialogs, popovers, and windows
- Minimum, restored, maximized, and high-DPI layouts
- Unsaved state on close, quit, crash recovery, and update restart
- Screen-reader names for custom canvas or toolbar controls

For mobile software, verify:

- Touch comfort and reachability
- On-screen keyboard avoidance
- Safe areas, rotation, font scaling, and interruption recovery
- Permission denial and settings recovery
- Offline, background, resume, and destructive gesture behavior

## Platform Evidence

The evidence artifact should name each supported platform and record the platform-specific workflows actually exercised. Do not claim native fit from a browser screenshot alone.

For each target platform, capture at least:

- Runtime and version
- Window or viewport state
- Input methods exercised
- Primary task outcome
- One platform-specific behavior
- Accessibility or scaling setting exercised when material
- Known unverified platform surfaces

## Sources

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Windows App Design](https://learn.microsoft.com/windows/apps/design/)
- [Fluent 2](https://fluent2.microsoft.design/)
- [Material Design](https://m3.material.io/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
