![ChatGPT Image Apr 5, 2025, 11_02_00 PM](https://github.com/user-attachments/assets/bc51b438-e8f1-4518-9176-020f9f19d507)


*Convert NEF files to PNG files, using parallel processing* (this implementation uses IrfanView, but you can use other methods to convert them, or even adjust this script to run your own "multi-tasking" tools.)

![nikon](https://user-images.githubusercontent.com/8074474/218271430-f0a30b60-a8da-4c3d-9042-3229ef641bac.jpg)


# NEF2PNG is a Python script
* that uses multiprocessing 
* to convert all NEF files in a folder to PNG format

## It improves process time ~4x on a 4-core processor.
Example (core i5 quad core)
* regular IrfanView conversion of 100 NEF (RAW) images to PNG format takes around 10 minutes
* with NEF2PNG, it takes ~2.5 minutes.

## Requires: 
### 1) IrfanView to do the conversion
### 2) more than one core to get a better performance than simply using Irfanview
 
This implementation runs on Windows, but the main idea should be able to run on Linux, try changing the main Conversion commands to their Linux applicable version.

Run the following command (in the command prompt on Windows) to execute NEF2PNG with Python.

**>python.exe NEF2PNG.py**
