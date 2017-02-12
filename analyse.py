from __future__ import division
import openpyxl
import pdftables_api
import pickle


users = {
	'apk'			:	('1', 'Ashok'),
	'pranay_ramani'	:	('12345','Pranay'),
	'saba_sayyed'	:	('12345','Saba'),
	'sonali_singh'	:	('12345','Sonali')
}
temp = 0
sub = []
sub1 = []
sub2 = []
sub3 = []
sub4 = []
sub5 = []
tot = [0,0,0,0,0]
#c = pdftables_api.Client('foj6gubij3o2')
#c.xlsx('001075.pdf', 'result.xlsx')

wb = openpyxl.load_workbook('Mahesh_output.xlsx')

sheet = wb.get_sheet_by_name('Sheet1')

#print sheet.value

#print sheet['A3'].value

for i in sheet['B3':'B7']:
	for j in i:
		sub.append(j.value)
	#print sub  	

for val in sheet['C3':'F3']:
	for k in val:
		sub1.append(k.value)
		#temp+= int(k.value)
		tot[0]+= int(k.value)
		#print k.value
	#sub1 += val.value

for val in sheet['C4':'F4']:
	for k in val:
		sub2.append(k.value)
		#tot2
		tot[1]+= int(k.value)
		#print k.value

for val in sheet['C5':'F5']:
	for k in val:
		sub3.append(k.value)
		tot[2]+= int(k.value)
		#print k.value

for val in sheet['C6':'F6']:
	for k in val:
		sub4.append(k.value)
		tot[3]+= int(k.value)
		#print k.value

for val in sheet['C7':'F7']:
	for k in val:
		sub5.append(k.value)
		tot[4]+= int(k.value)
		#print k.value

#print sub1, sub2, sub3, sub4, sub5

#print tot1, tot2, tot3, tot4, tot5

res_details = {
	'Name' 		: sheet['A3'].value,
	#below line doesn't work :(, will have to hardcode values
	# 'Subjects'	: sheet['B3':'B7'].value
	'Subjects'	: sub

}

#print res_details
print "****************************"
print "Welcome to E-Result Analysis"
print "****************************\n"
print "Enter the user credentials:\n"

u_id = raw_input("User ID: ")
pass_ = raw_input("Password: ")

# block used to add users
with open("list_of_users.txt",'w') as fp:
	#for user,pass_ in users.iteritems():
	pickle.dump(users,fp)

with open("list_of_users.txt",'rb') as fp:
	ver_list = pickle.load(fp)
	fp.seek(0)

for user,password in ver_list.iteritems():
	if user == u_id and password[0] == pass_:
		print "\nWelcome "+password[1]+"!"

		choice = input("\nWhat would you like to do?\n\t1. Display full report \n\t2. Display status(Pass/Fail) \n\t3. Subject-wise marks \nChoice: ")
		if choice == 1:
			#pass
			print "Displaying report..."
			print "\tStudent name: "+res_details['Name']
			print "\tSubject totals: "
			for p in range(0,5):
				print "\t\t"+res_details['Subjects'][p]+"\t:"+str(tot[p])
			print "\tTotal\t\t:"+str(sum(tot))
			print "\tMax marks\t:"+str(max(tot))
			print "\tMin marks\t:"+str(min(tot))
			#print len(tot)
			#num = sum(tot)
			#den = (len(tot)*125)
			#print float(num//den)
			perc = (sum(tot)/(len(tot)*125))*100
			if perc < 35:
				print "\tStatus: Fail\n\tYou've scored "+str(perc)+"%"	
			else:
				print "\tStatus: Pass!\n\tYou've scored "+str(perc)+"%"

		elif choice == 2:
			perc = (sum(tot)/(len(tot)*125))*100
			if perc < 35:
				print "\tStatus: Fail\n\tYou've scored "+str(perc)+"%"	
			else:
				print "\tStatus: Pass!\n\tYou've scored "+str(perc)+"%"
		elif choice == 3:
			print "Subject-wise marks..."
			for p in range(0,5):
				print "\t\t"+res_details['Subjects'][p]+"\t:"+str(tot[p])
	#else: 
	#	print "Sorry, user not registered!"
	#	break