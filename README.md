# kaiyu_odor_rig

Authors:

    Peter Polidoro <polidorop@janelia.hhmi.org>

License:

    BSD

##Example Usage

[Example Protocol File](./example_protocol.yaml)

Open a terminal and enter:

```shell
cd ~/kaiyu_odor_rig
ipython
```

In iPython enter:

```python
from kaiyu_odor_rig import KaiyuOdorRig
odor_rig = KaiyuOdorRig()
odor_rig.setup_mfcs('example_mfc_settings.yaml')
odor_rig.run_protocol('example_protocol.yaml')
```

##Installation

###Linux

Open a terminal and enter:

```shell
sudo apt-get install git -y
cd ~
git clone https://github.com/peterpolidoro/kaiyu_odor_rig.git
sudo pip install ipython
sudo pip install modular_device
sudo pip install pyyaml
```

On linux, you may need to add yourself to the group 'dialout' in order
to have write permissions on the USB port:

Open a terminal and enter:

```shell
sudo usermod -aG dialout $USER
sudo reboot
```
