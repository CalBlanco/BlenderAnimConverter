# Convert Blender animation pngs name000X.png into directional names

## Usage

Drag folders of images / images into the directory this script is in and run the script

It will rename blender animation images in to a file name that is better for our atlas 

### Requirements

Make sure to name your blender output to `<name>-` the `-` will ensure that all images by blender are named `<name>-000X` where X is the animation number. 

The animation numbers are translated as follows
`0001` = `right`
`0002` = `left`
`0003` = `bottom`
`0004` = `top`

### Walls
For walls this direction implies the quadrant  the wall will be placed in

### Objects
For objects this direction informs us which direction the "front-face" of the object is


## Results
This script will rename images inplace **make sure to use a copy**
