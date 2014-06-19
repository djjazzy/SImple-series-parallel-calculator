#!usr/bin/python
#PYthon 2.7, IDE = Geany

import Tkinter as tk

class ParSerCal(tk.Tk):
	
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Parallel and Series Resistor Configurator")
		
		self.cbDict={"cb0" : 1, "cb1" : 1, "cb2" : 1, "cb3" : 1,
					 "cb4" : 1, "cb5" : 1, "cb6" : 1, "cb7" : 1,
					 "cb8" : 1, "cb9" : 1, "cb10" : 1, "cb11" : 1,
					 "cb12" : 1, "cb13" : 1}
					 
		self.rbDict={"rbs0" : 1, "rbs1" : 1, "rbs2" : 1, "rbs3" : 1,
					 "rbs4" : 1, "rbs5" : 1, "rbs6" : 1, "rbs7" : 1,
					 "rbs8" : 1, "rbs9" : 1, "rbs10" : 1, "rbs11" : 1,
					 "rbs12" : 1, "rbs13" : 1, "rbs14" : 1, "rbs15" : 1,
					 "rbs16" : 1, "rbs17" : 1, "rbs18" : 1, "rbs19" : 1,
					 "rbs20" : 1, "rbs21" : 1, "rbs22" : 1, "rbs23" : 1,
					 "rbs24" : 1, "rbs25" : 1, "rbs26" : 1, "rbs27" : 1}
					 
		# Set cbDict value variable type and init variables for cbDict keys
		for cb in self.cbDict.keys():
			self.cbDict[cb] = tk.IntVar()
			self.cbDict[cb].set(0)
			
		# Set rbDict value variables and init variables rbDict keys 	
		for rb in self.rbDict.keys():
			self.rbDict[rb] = tk.IntVar()
			self.rbDict[rb].set(1)
			
		resDispFrame = tk.LabelFrame(self, text="Resistor Selection")
		
		# Resistances. Series and parallel lists for adding later to get total resistance
		self.resList = [25,25, 25, 40 , 50, 50, 50, 100, 100, 200, 200, 300, 300, 560];
		self.seriesList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.parallelList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		
		self.cBoxDict = {"cBox0":self.cbDict["cb0"], "cBox1":self.cbDict["cb1"],
						 "cBox2":self.cbDict["cb2"], "cBox3":self.cbDict["cb3"],
						 "cBox4":self.cbDict["cb4"], "cBox5":self.cbDict["cb5"],
						 "cBox6":self.cbDict["cb6"], "cBox7":self.cbDict["cb7"],
						 "cBox8":self.cbDict["cb8"], "cBox9":self.cbDict["cb9"],
						 "cBox10":self.cbDict["cb10"], "cBox11":self.cbDict["cb11"],
						 "cBox12":self.cbDict["cb12"], "cBox13":self.cbDict["cb13"]}
		
		self.rbBoxDict = {"psSetP0":self.rbDict["rbs0"], "psSetP1":self.rbDict["rbs1"],
						  "psSetP2":self.rbDict["rbs2"], "psSetP3":self.rbDict["rbs3"],
						  "psSetP4":self.rbDict["rbs4"], "psSetP5":self.rbDict["rbs5"],
						  "psSetP6":self.rbDict["rbs6"], "psSetP7":self.rbDict["rbs7"],
						  "psSetP8":self.rbDict["rbs8"], "psSetP9":self.rbDict["rbs9"],
						  "psSetP10":self.rbDict["rbs10"], "psSetP11":self.rbDict["rbs11"],
						  "psSetP12":self.rbDict["rbs12"], "psSetP13":self.rbDict["rbs13"],
						  "psSetP14":self.rbDict["rbs14"], "psSetP15":self.rbDict["rbs15"],
						  "psSetP16":self.rbDict["rbs16"], "psSetP17":self.rbDict["rbs17"],
						  "psSetP18":self.rbDict["rbs18"], "psSetP19":self.rbDict["rbs19"],
						  "psSetP20":self.rbDict["rbs20"], "psSetP21":self.rbDict["rbs21"],
						  "psSetP22":self.rbDict["rbs22"], "psSetP23":self.rbDict["rbs23"],
						  "psSetP24":self.rbDict["rbs24"], "psSetP25":self.rbDict["rbs25"],
						  "psSetP26":self.rbDict["rbs26"], "psSetP27":self.rbDict["rbs27"]}
						  
		# Declare all of the checkboxes
		i=0			  
		for cbx in self.cBoxDict.keys():
			self.cBoxDict[cbx] = tk.Checkbutton(resDispFrame, text=str(self.resList[i]), variable = self.cbDict["cb" + str(i)])
			i+=1
		
		# Declare all of the radio buttons
		i,j=0,0
		for pss in self.rbBoxDict.keys():
			if i%2==0:
				self.rbBoxDict[pss] = tk.Radiobutton(resDispFrame, text="Series", variable = self.rbDict["rbs"+str(j)], value = 1)
			else:
				self.rbBoxDict[pss] = tk.Radiobutton(resDispFrame, text="Parallel", variable = self.rbDict["rbs"+str(j)], value = 2)
				j+=1
			i+=1
		
		self.ansFrame = tk.LabelFrame(self, text = "Resistance")
		self.resLabel = tk.Label(self.ansFrame, text="R = ", font = '15')
		self.resAns = tk.Label(self.ansFrame, text = "0", font = '15', fg='blue')
		
		# Put widgets on windows ***********
		resDispFrame.grid(row=0, column=0)
		
		# Put all of the checkboxes on the window
		r = 0
		for cbx in self.cBoxDict.keys():
			self.cBoxDict[cbx].grid(row=r, column=0)
			r+=1
		
		# Put all of the radio buttons on the window
		k,j=0,0
		for rb in self.rbBoxDict.keys():
			if k%2==0:
				self.rbBoxDict[rb].grid(row=j, column=1)
			else:
				self.rbBoxDict[rb].grid(row=j, column=2)
				j+=1
			k+=1
		
		self.ansFrame.grid(row=1, column=0)
		self.resLabel.grid(row=0, column=0)
		self.resAns.grid(row=0, column=1)
		
		self.calcRunFunction()
	
	# Helper Funcs *************************************
	
	# Seperate series values from parallel values	
	def seperateSP(self):
		for p in range(0,14):
			if self.cbDict["cb"+str(p)].get() == True:
				if self.rbDict["rbs"+str(p)].get() == True:
					self.parallelList[p]=0
					self.seriesList[p] = self.resList[p]
				else:
					self.seriesList[p] = 0
					self.parallelList[p] = self.resList[p]
			else:
				self.seriesList[p] = 0
				self.parallelList[p] = 0
			p+=1
		
	def getSeriesResult(self):
		r,i=0,0
		for i in range(0, 14):
			r = r + self.seriesList[i]
			i = i+1
		return r
			
	def getParallelResult(self):
		r, i = 0.0, 0
		for i in range(0,14):
			if self.parallelList[i]<=0:
				pass
			else:
				r = r + 1.0/(self.parallelList[i])
				i = i+1
		if r != 0:
			r = 1.0/r
		return r
		
	def calcRunFunction(self):
		self.seperateSP()	
		series = self.getSeriesResult()
		parallel = self.getParallelResult()
		res = series + parallel
		self.resAns.configure(text=str(res))
			
		self.after(200, self.calcRunFunction)
		
parser = ParSerCal()
parser.mainloop()
