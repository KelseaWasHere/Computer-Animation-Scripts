def animate_light_intensity():
    # Get all lights in the scene
    all_lights = cmds.ls(type=['pointLight', 'directionalLight', 'spotLight'])

    # Iterate through each light and animate intensity
    for light in all_lights:
        # Clear previous keyframes
        cmds.cutKey(light, time=(1, cmds.playbackOptions(q=True, maxTime=True)))

        # Get current intensity
        current_intensity = cmds.getAttr(f'{light}.intensity')

        # Set keyframes for intensity
        cmds.setKeyframe(light, attribute='intensity', time=1, value=current_intensity)
        cmds.setKeyframe(light, attribute='intensity', time=cmds.playbackOptions(q=True, maxTime=True), value=current_intensity * 1.75)

# Run the script
animate_light_intensity()