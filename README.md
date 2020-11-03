# GPS
GPS module sends the data related to tracking position in real time, and it sends so many data in NMEA format . NMEA format consist several sentences, in which we only need one sentence. This sentence starts from $GPGGA and contains the coordinates, time and other useful information. This GPGGA is referred to Global Positioning System Fix Data. 
 
From these data we can extract coordinate from $GPGGA string by counting the commas in the string.
The $ GPGGA format:
$GPGGA,HHMMSS.SSS,latitude,N,longitude,E,FQ,NOS,HDP,altitude,M,height,M,,checksum data
