#Example Sound Level Sketch for the Adafruit Microphone Amplifier

sampleWindow = 10000; # Sample window width in mS (10s = 10000 mS = 0.1 Hz)
unsigned int sample;

#arduino code
void setup()
{
   Serial.begin(9600);
}


# arduino code
# void loop()

{
   unsigned long startMillis= millis();  # Start of sample window
   unsigned int peakToPeak = 0;   #peak-to-peak level

   unsigned int signalMax = 0;
   unsigned int signalMin = 1024;

   # collect data for 10000 mS
   while (millis() - startMillis < sampleWindow)
   {
      sample = analogRead(0);
      if (sample < 1024)  // toss out spurious readings
      {
         if (sample > signalMax)
         {
            signalMax = sample;  // save just the max levels
         }
         else if (sample < signalMin)
         {
            signalMin = sample;  // save just the min levels
         }
      }
   }
   peakToPeak = signalMax - signalMin;  # max - min = peak-peak amplitude
   double volts = (peakToPeak * 5.0) / 1024;  #  convert to volts

   Serial.println(volts);
}