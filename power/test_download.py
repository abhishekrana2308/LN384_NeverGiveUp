import pandas as pd

minms = {'Actual_flow':6020, 'Frequency':55}
maxms = {'Actual_flow':6200, 'Frequency':65}
def getfile(path, minms, maxms):
	csv_file = pd.read_csv(path)
	ac = csv_file['Actual_flow']
	freq = csv_file['Frequency']
	date = csv_file['Date_updated']

	ret = []
	for i in range(0,csv_file.shape[0]):
		ac_cur = ac[i]
		freq_cur = freq[i]
		date_cur = date[i]

		if ac_cur<minms['Actual_flow'] or ac_cur>maxms['Actual_flow']:
			if ac_cur<minms['Actual_flow']:
				res = {'Actual_flow' : ac_cur, 'Frequency' : freq_cur, 'Date_updated' : date_cur, 'Message' : 'Actual Flow is less than ATC'}
			else:
				res = {'Actual_flow' : ac_cur, 'Frequency' : freq_cur, 'Date_updated' : date_cur, 'Message' : 'Actual Flow is more than ATC'}
			ret.append(res)
		elif freq_cur<minms['Frequency'] or freq_cur>maxms['Frequency']:
			if freq_cur<minms['Frequency']:
				res = {'Actual_flow' : ac_cur, 'Frequency' : freq_cur, 'Date_updated' : date_cur, 'Message' : 'Less Frequency used'}
			else:
				res = {'Actual_flow' : ac_cur, 'Frequency' : freq_cur, 'Date_updated' : date_cur, 'Message' : '<More Frequency used'}
			ret.append(res)

	return ret




print(getfile("./download/Notice 2020 - Sheet1.csv",minms,maxms))