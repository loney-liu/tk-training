import sgtk

HookClass = sgtk.get_hook_baseclass()


class SceneOperation(HookClass):
    def scan_scene(self):
        """
        The scan scene method is executed once at startup and its purpose is
        to analyze the current scene and return a list of references that are
        to be potentially operated on.
        The return data structure is a list of dictionaries. Each scene reference
        that is returned should be represented by a dictionary with three keys:
        - "node": The name of the 'node' that is to be operated on. Most DCCs have
          a concept of a node, path or some other way to address a particular
          object in the scene.
        - "type": The object type that this is. This is later passed to the
          update method so that it knows how to handle the object.
        - "path": Path on disk to the referenced object.
        Toolkit will scan the list of items, see if any of the objects matches
        any templates and try to determine if there is a more recent version
        available. Any such versions are then displayed in the UI as out of date.
        """
        engine = self.parent.engine
        operations = engine.operations

        return operations.get_references()

    def update(self, items):
        """
        Perform replacements given a number of scene items passed from the app.
        Once a selection has been performed in the main UI and the user clicks
        the update button, this method is called.
        The items parameter is a list of dictionaries on the same form as was
        generated by the scan_scene hook above. The path key now holds
        the that each node should be updated *to* rather than the current path.
        """
        engine = self.parent.engine
        operations = engine.operations

        engine.logger.debug("Updating scene {}".format(items))
        operations.update_scene(items)