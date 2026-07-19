# Specialized Surfaces

Read this reference when the interface extends beyond conventional web, mobile, or desktop application patterns.

## Contents

- Messaging And Collaboration
- Maps And Spatial Operations
- Kiosks And Shared Devices
- TV And Ten-Foot Interfaces
- Wearables And Glanceable UI
- Automotive Interfaces
- Spatial And XR Interfaces
- Voice And Multimodal Interfaces
- Cross-Surface Continuity
- Verification

## Messaging And Collaboration

- Make authorship, time, delivery, editing, threading, mentions, and unread state clear.
- Preserve context when replying, quoting, forwarding, searching, or switching channels.
- Distinguish drafts, pending sends, failures, retries, and offline state.
- Protect private, public, external, and restricted audience boundaries.
- Keep composer controls secondary to the conversation unless creation is the primary task.
- Handle long histories, attachments, reactions, moderation, and deleted content without losing orientation.

## Maps And Spatial Operations

- Keep the map or spatial field dominant when location is the primary object.
- Separate geographic state from list, filter, route, incident, or asset state while keeping selection synchronized.
- Provide non-map alternatives for critical information and actions.
- Define zoom, clustering, overlap, labels, uncertainty, stale location, and unavailable tiles.
- Avoid encoding status only through marker color.
- Preserve orientation when panels open, routes update, or live data moves.

## Kiosks And Shared Devices

- Assume public visibility, interrupted sessions, unfamiliar users, and limited assistance.
- Use large targets, short paths, explicit progress, and clear timeout behavior.
- Protect personal data from the next user and clear sessions reliably.
- Handle printers, scanners, payment devices, cameras, network loss, and peripheral failure.
- Avoid hover, hidden gestures, and controls near inaccessible screen edges.
- Provide language and accessibility choices before the main task when required.

## TV And Ten-Foot Interfaces

- Design for distance, directional focus, remote input, overscan or safe areas, and limited text entry.
- Keep focus highly visible and movement predictable.
- Use fewer, larger choices and protect reading size at viewing distance.
- Avoid dense grids, pointer-dependent controls, and long forms.
- Preserve playback, selection, and navigation state when overlays appear.
- Test with the actual remote or gamepad interaction model.

## Wearables And Glanceable UI

- Prioritize one immediate piece of information or one short action.
- Design for brief attention, small surfaces, motion, outdoor contrast, and one-handed interaction.
- Use complications, notifications, haptics, voice, and paired-device handoff according to platform conventions.
- Avoid shrinking a phone screen into a watch.
- Keep destructive or consequential work on a larger trusted surface when appropriate.
- Support text scaling and reduced motion without hiding the primary state.

## Automotive Interfaces

- Minimize visual demand, interaction duration, precision, memory load, and text entry.
- Separate parked-only functionality from driving-safe functionality.
- Prefer voice, steering controls, large targets, and brief glanceable feedback where the platform allows them.
- Never let decorative motion compete with road-critical information.
- Follow the vehicle platform, legal, and safety requirements rather than generic mobile patterns.
- Test interruption, audio focus, connectivity loss, night mode, and driver or passenger context.

## Spatial And XR Interfaces

- Treat depth, scale, reach, field of view, comfort, anchoring, and occlusion as layout constraints.
- Keep primary controls within comfortable viewing and interaction regions.
- Avoid placing essential information behind users or over moving backgrounds without stabilization.
- Provide alternatives for gestures, gaze, voice, controllers, and mobility limitations.
- Use spatial audio and motion only when they clarify location or causality.
- Test fatigue, locomotion, focus transitions, passthrough, boundaries, and interruption recovery.

## Voice And Multimodal Interfaces

- Make listening, processing, confirmation, error, privacy, and recording state explicit.
- Confirm high-consequence commands and ambiguous entities.
- Provide visual or touch alternatives when speech is unavailable, inappropriate, or inaccessible.
- Keep prompts short and allow interruption, correction, repetition, and cancellation.
- Do not expose sensitive information aloud without context-aware safeguards.
- Preserve one coherent task state across voice, keyboard, touch, and pointer input.

## Cross-Surface Continuity

- Share objects, terminology, account state, and task progress across devices.
- Adapt navigation, density, controls, and input to each surface instead of cloning layouts.
- Define which device owns capture, review, confirmation, payment, recovery, and notification.
- Make handoff and synchronization status visible.
- Handle conflicts, stale data, partial completion, and offline work.

## Verification

Use the real device, simulator, or target input model when practical. Verify:

1. Viewing distance, reach, focus, and input method
2. Primary task and one interruption or failure path
3. Personal-data exposure on shared or ambient surfaces
4. Platform accessibility settings
5. Peripheral, connectivity, and lifecycle behavior
6. Handoff and synchronization when multiple surfaces participate
