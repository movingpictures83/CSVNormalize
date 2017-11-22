import sys
import numpy



class CSVNormalizePlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      print(self.bacteria)
      self.ADJ = numpy.zeros([self.m, self.n])
      i = 0
      for i in range(self.m):
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               print i, j, self.m, self.n, len(contents)
               value = float(contents[j+1])
               #print self.ADJ[i][j]
               self.ADJ[i][j] = value
            i += 1

      sums = []
      print "M: ", self.m, " ", "N: ", self.n
      for j in range(self.m):
         sums.append(0)
         for i in range(self.n):
            sums[j] += self.ADJ[j][i]
         print "SUM FOR SAMPLE ", j, ": ", sums[j]

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write(self.firstline+'\n')
      for i in range(self.m):
         sum = float(0.0)
         for j in range(self.n):
            sum += self.ADJ[i][j]
         #print "SUM: ", sum
         for j in range(self.n):
            self.ADJ[i][j] /= sum
            
      for i in range(self.m):
         #filestuff2.write(self.bacteria[i]+',')
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



