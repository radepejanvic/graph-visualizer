from typing import List, Union
from api.src.api.services.base import DataSourceBase, VisualizerBase
from core import Core


def console_menu(core: Core):
    plugins: List[Union[DataSourceBase, VisualizerBase]] = \
        core.data_sources + core.visualizers

    if not plugins:
        print("No plugins found!")
        return

    error = False
    message = None
    while True:
        print("-----------------------------------")
        if error:
            print("Wrong input!")
            error = False
        if message:
            print(message)
        print("Choose the option: ")

        for i, plugin in enumerate(plugins):
            print(f"{i}) {plugin.identifier()} - {plugin.name()}")
        print("X - exit")
        try:
            choice = input("Enter the ordinal number of the option: ")
        except:
            error = True
            continue
        if choice.upper() == "X":
            return
        elif 0 <= int(choice) < len(plugins):
            message = chosen_option(plugins[int(choice)], core)
        else:
            error = True


def chosen_option(plugin: Union[DataSourceBase, VisualizerBase], core: Core):
    try:
        if isinstance(plugin, DataSourceBase):
            core.graph = plugin.load()
        elif isinstance(plugin, VisualizerBase):
            return plugin.display(core.graph)
    except Exception as e:
        print(f"Error: {e}")


def main():
    try:
        core = Core()
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        console_menu(core)
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
