import maya.cmds as cmds

def apply_parent_constraint():
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)

    # Check if at least three objects are selected
    if len(selected_objects) < 3:
        print("Error: You must select at least three clips.")
        return

    # Get the first three selected objects
    parent_objects = selected_objects[:3]

    # Loop through the child objects (excluding the parent objects)
    for child_object in selected_objects[3:]:
        # Create a parent constraint for each child object to its corresponding parent object
        parent_index = selected_objects.index(child_object) % 3
        parent_object = parent_objects[parent_index]
        constraint_name = cmds.parentConstraint(parent_object, child_object, maintainOffset=False)
        print(f"Parent constraint applied: {child_object} is now a child of {parent_object}")

# Call the function
apply_parent_constraint()