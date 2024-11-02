import omni.ui as ui
from omni.kit.window.filepicker import FilePickerDialog
from pxr import Usd, UsdGeom
import asyncio

class UsdFileViewerApp:
    def __init__(self):
        self.current_file_path = None
        self.stage = None

        # Create the UI window
        self.window = ui.Window("USD File Info Viewer", width=400, height=200)
        with self.window.frame:
            with ui.VStack(spacing=10):
                # Select USD row: Button and Filename Label
                with ui.HStack(spacing=10):
                    self.open_dialog_button = ui.Button("Select USD", clicked_fn=self.open_file_dialog)
                    self.file_name_label = ui.Label("No file selected", alignment=ui.Alignment.LEFT)

                # Up Axis row
                with ui.HStack(spacing=10):
                    ui.Label("Up Axis")
                    self.up_axis_selection = ui.ComboBox(3, "X", "Y", "Z","AA")

                # Units row
                with ui.HStack(spacing=10):
                    ui.Label("Units")
                    self.units_input = ui.FloatField()

                # Action buttons: Apply and Clear
                with ui.HStack(spacing=10):
                    self.apply_button = ui.Button("Apply Changes", clicked_fn=self.apply_changes)
                    self.clear_button = ui.Button("Clear File", clicked_fn=self.clear_selection)

    def open_file_dialog(self):
        print("Open File")
        # Open a FilePickerDialog
        self.file_picker_dialog = FilePickerDialog(
            title="Select a USD File",
            width=600,
            height=400,
            click_apply_handler=self.on_file_selected_wrapper,
            click_cancel_handler=self.on_cancel_selection,
            file_extension_options=[
                (".usd", "USD Files"),
                (".usda", "USD ASCII Files"),
                (".usdc", "USD Binary Files"),
                (".usdz", "USD Zip Files")
            ]
        )

    def on_file_selected_wrapper(self, file_name: str, dir_name: str):
        # Wrapper to run the async function
        asyncio.ensure_future(self.on_file_selected(file_name, dir_name))
        print("Async")

    async def on_file_selected(self, file_name: str, dir_name: str):
        print("Loading")
        usd_file_path = f"{dir_name}/{file_name}"

        try:
            # Use asyncio.to_thread to run Usd.Stage.Open in a separate thread
            self.stage = await asyncio.to_thread(Usd.Stage.Open, usd_file_path) 
            if not self.stage:
                raise RuntimeError("Failed to open USD file.")

            self.current_file_path = usd_file_path
            self.file_name_label.text = file_name

            # Get up axis and meters per unit
            self.selected_up_axis = UsdGeom.GetStageUpAxis(self.stage)
            self.selected_meters_per_unit = UsdGeom.GetStageMetersPerUnit(self.stage)

            # Populate UI elements (simplified)
            if self.selected_up_axis == "X":
                self.up_axis_selection.model.get_item_value_model().set_value(0)
            elif self.selected_up_axis == "Y":
                self.up_axis_selection.model.get_item_value_model().set_value(1)
            elif self.selected_up_axis == "Z":
                self.up_axis_selection.model.get_item_value_model().set_value(2)
            else:
                self.up_axis_selection.model.get_item_value_model().set_value(2)

            self.units_input.model.set_value(self.selected_meters_per_unit)

        except Exception as e:
            print(f"Error loading USD file: {e}")  # Print the exception for debugging
            carb.log_error(f"Error loading USD file: {e}")  # Log the error
            self.file_name_label.text = "Error loading USD file"
            self.clear_selection() 

        finally:
            # Ensure dialog is closed even if there's an error
            self.file_picker_dialog.destroy() 

    def on_cancel_selection(self, file_name: str, dir_name: str):
        async def destroy_self_async():
            self.file_picker_dialog.destroy()
            print("[hlplanning.usd.scaleupaxis] Destroy File Picker Window (async)")

        asyncio.ensure_future(destroy_self_async())


    def apply_changes(self):
        if self.stage and self.current_file_path:
            # Apply the selected up axis and meters per unit to the stage
            print("[hlplanning.usd.scaleupaxis] Applying Changes")
            selected_index = self.up_axis_selection.model.get_item_value_model(0).get_value_as_int()
            selected_up_axis = "X" if selected_index == 0 else "Y"
            meters_per_unit = self.units_input.model.get_value_as_float()

            UsdGeom.SetStageUpAxis(self.stage, selected_up_axis)
            UsdGeom.SetStageMetersPerUnit(self.stage, meters_per_unit)

            # Save the changes to the USD file
            self.stage.GetRootLayer().Save()

            # Update labels to confirm save
            self.file_name_label.text = f"Changes applied to {self.file_name_label.text}"

    def clear_selection(self):
        # Reset all UI elements and clear file path
        print("[hlplanning.usd.scaleupaxis] Clear")
        self.current_file_path = None
        self.stage = None
        self.file_name_label.text = "No file selected Dummy"
        self.units_input.model.set_value(value=1.0)  # Default to 1.0 meters per unit
        self.up_axis_selection.model.get_item_value_model().set_value(2)

# Run the app
UsdFileViewerApp()
