# USD File Attribute Standardizer

A simple Omniverse extension for managing and standardizing USD file attributes like **units** and **up axis**. This tool makes it easy to modify these settings across multiple files, ensuring consistent results when combining assets from different programs such as SketchUp, CityEngine, Blender, and NVIDIA’s assets.

## Why This Tool?

When working with USD files from different applications, the units and up axis often vary, leading to unintended results when combining or layering these assets. This extension provides a straightforward way to:

- **Set the Up Axis** (Y or Z)
- **Define Units in Meters per Unit**

By standardizing these attributes, you can ensure your files align consistently in Omniverse, avoiding misalignments and scaling issues.

## Features

- **Select USD File**: Quickly browse and select any USD file you want to standardize.
- **View and Set Attributes**:
    - **Up Axis**: Choose between "Y" or "Z" axis orientation.
    - **Units**: Define the units in meters to ensure consistent scaling.
- **Apply Changes**: Save your changes to the USD file directly.
- **Clear Selection**: Reset the UI to make new selections.

## Installation

1. Clone this repository into your Omniverse extensions folder:
    
    bash
    
    Copy code
    
    `git clone https://github.com/yourusername/USD-File-Attribute-Standardizer.git`
    
2. Enable the extension in the Omniverse Kit Extensions Manager.
    

## Usage

1. **Open the Extension**:
    
    - In Omniverse, navigate to the extension panel and launch the "USD File Attribute Standardizer."
2. **Select a USD File**:
    
    - Click the **"Select USD"** button to open a file picker dialog.
    - Choose the USD file you want to standardize. The file name and its current attributes (Up Axis and Units) will display in the UI.
3. **Modify Attributes**:
    
    - **Up Axis**: Use the dropdown to select either **"Y"** or **"Z"**.
    - **Units**: Enter the desired units in meters per unit.
4. **Apply Changes**:
    
    - Click **"Apply Changes"** to save the modifications directly to the USD file.
    - The UI will confirm when changes have been successfully applied.
5. **Clear Selection**:
    
    - Use the **"Clear File"** button to reset the extension, allowing for a new file selection.

## Example Use Case

If you’re merging assets from **SketchUp** (typically using Y-Up) and **Blender** (which may use Z-Up), you can use this extension to quickly align the up axis and units, ensuring all files match the same orientation and scale before integration.

## Contributing

Contributions are welcome! Please submit issues and pull requests to help improve this tool.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.