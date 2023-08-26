# OpenCV REPO
Explain how to install Open CV on Ubuntu 20.04 on the DELL G15

## OpenCV Quick Start

Install mininmal pre reqs
```
    $ sudo apt update && sudo apt install -y cmake g++ wget unzip
```

Download and upnpack
```
    $ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
    $ unzip opencv.zip
```

Create build directory
```
mkdir -p build && cd build
```

Configure "x" (set to which versio you want)
```
cmake ../opencv-4.x
```

Build
```
    $cmake --build . 
```
Thank you https://github.com/Asadullah-Dal17 for helping out!
