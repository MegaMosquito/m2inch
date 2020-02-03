FROM raspbian/stretch:latest
WORKDIR /

# Dockerized code for this $15 screen:
#    https://smile.amazon.com/gp/product/B081Q79X2F/ref=ppx_yo_dt_b_asin_title_o05_s01?ie=UTF8&psc=1

# Install build tools
RUN apt update && apt install -y \
  python3 python3-dev python3-pip \
  wget curl jq make

#apk --no-cache --update add gawk bc socat git gcc libc-dev linux-headers scons swig wget curl jq make

# Install BCM2835 chip (for Raspberry Pi) support
RUN wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
RUN tar zxvf bcm2835-1.60.tar.gz
RUN cd /bcm2835-1.60/; ./configure
RUN cd /bcm2835-1.60/; make
#RUN cd /bcm2835-1.60/; make check
RUN cd /bcm2835-1.60/; make install

# Install the python GPIO library
RUN pip3 install RPi.GPIO

# Install the python SPI library
RUN pip3 install spidev

# Install the python WiringPi library
RUN pip3 install wiringpi

# Install the python imaging library
RUN apt install -y python3-pil

# Install the python numpy library
RUN pip3 install numpy

# Install the atlas library
RUN apt install -y libatlas-base-dev

# Install flask (for the REST API server)
RUN pip3 install Flask

# Install the driver for the Waveshare 2inch ST7789 SPI LCD
RUN apt install -y p7zip-full
RUN wget http://www.waveshare.net/w/upload/1/19/2inch_LCD_Module_code.7z
RUN 7z x 2inch_LCD_Module_code.7z  -r -o./2inch_LCD_Module_code
RUN chmod 777 -R  2inch_LCD_Module_code

# Copy over the daemon code
COPY ./m2i_server.py /

# Run the daemon
CMD python3 /m2i_server.py

