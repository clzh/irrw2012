# Introduction #

The [object\_tracker](http://ros.org/wiki/object_tracker) package provides tracking of objects of interest such as victims and QR codes.

# Details #
Objects can be added using either a topic based interface (in case of continuously incoming percepts, for example from a thermal camera) or via services. We concentrate on the service based interface in this tutorial.

The most important service is [AddObject](http://ros.org/doc/fuerte/api/worldmodel_msgs/html/srv/AddObject.html). An example of it being used in a [rqt\_gui](http://ros.org/wiki/rqt_gui) based dialog plugin is available [here](https://code.google.com/p/irrw2012/source/browse/trunk/rqt_rescue_control_plugin/lib/RescueControlDialog.py#59).