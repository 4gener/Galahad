# Galahad

### Description

This project is designed to monitor the devices' occupancy of the laundry rooms which are under the administration of **Lunan Information and Technology Co., Ltd**(伦安信息科技有限公司). Information in `config.json` are matches for student dormitory buildings' number and url in Tongji Univ, Jiading Campus.

### Prerequisites

* Python environment

* installation of following python libraries

  `bs4`  `requests` 

### Run

```
$ python main.py
```

### Function

- [x] Obtain devices' serial numbers and occupancy
- [x] Obtain estimated time of finishing current task
- [x] Send notification when finding a unoccupied device
- [x] Support choosing multiple laundry rooms
- [ ] Support choosing different type of devices

### Update Log

> Version 2.0		__2017.8.31__

​	* Support choosing laundry rooms

​	* Support displaying machines' type

> Version 1.0 		__2017.7.14__

​	* Initial Commit
