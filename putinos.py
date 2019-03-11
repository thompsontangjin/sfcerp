# -*- codinng:utf-8 -*-
import pandas as pd

def dropduplicates(d,a):
	result=d[a].drop_duplicates().tolist()
	return result
def getpacklist():
	df=pd.read_excel("packlist/packlist.xlsx")
	dwl=dropduplicates(df,'wana')
	for dwle in dwl:
		dfwa=df[df['wana']==dwle]
		dfwal=dropduplicates(dfwa,'puno')
		for dfwap in dfwal:
			onepunopl= dfwa[dfwa['puno']==dfwap].reset_index(drop=True)[['mana','banu','exda','past','pagw','drums','wana']]
			lp=0
			while lp<len(onepunopl):
				print onepunopl.ix[lp]
				lp=lp+1




if __name__=='__main__':
	getpacklist()









