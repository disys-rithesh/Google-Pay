import getpay

Rithesh=getpay.Google_pay("Rithesh.Kishore@gmail.com","9003085347","RitheshKishore")
Rithesh.open_gpay()
Rithesh.email_verification()
Rithesh.mobile_verification()
Rithesh.name_verification()
Rithesh.otp_verification(15698,15698)
Rithesh.Bank_verification()
Rithesh.PanCard_Verification()
Rithesh.set_Pin("5384")
Rithesh.Enter_your_Pin(3465,3465)

class Phone_pe(getpay.Google_pay):                                                                                                            #INHERITANCE
    def __init__(slef,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

    def open_phonepe(self):
        print("Phone pe")
        
Kishore=Phone_pe("Rithesh23@gmail.com","9003085347","Rithesh")
Kishore.open_phonepe()
Kishore.mobile_verification()
Kishore.name_verification()
Kishore.otp_verification(780965,780965)
Kishore.Bank_verification()
Kishore.PanCard_Verification()
Kishore.set_Pin("238790")
Kishore.Enter_your_Pin(3564,3564)


        
googlepay=[{"name":"Rithesh","gpaynum":7397266887,"type":"personal","transaction":"regular"},                                           #DICTIONARY INSIDE LIST
           {"name":"kannan","gpaynum":9710405288,"type":"personal","transaction":"rare"},
           {"name":"karthi","gpaynum":8778799456,"type":"personal","transaction":"regular"},
           {"name":"kavitha","gpaynum":9840042296,"type":"personal","transaction":"regular"},
           {"name":"keerthi","gpaynum":7305066119,"type":"personal","transaction":"rare"},
           {"name":"kingsley","gpaynum":8754554295,"type":"personal","transaction":"regular"},
           {"name":"kiran","gpaynum":6383634327,"type":"personal","transaction":"rare"},
           {"name":"kiruthika","gpaynum":9789029339,"type":"personal","transaction":"regular"},
           {"name":"kowsalya","gpaynum":7871125838,"type":"personal","transaction":"regular"},
           {"name":"kowsi","gpaynum":7448744931,"type":"personal","transaction":"rare"},
           {"name":"kumar","gpaynum":7358565943,"type":"personal","transaction":"regular"},
           {"name":"lekha","gpaynum":7305772128,"type":"personal","transaction":"regular"},
           {"name":"lokesh","gpaynum":7358479530,"type":"personal","transaction":"regular"},
           {"name":"monisha","gpaynum":6383188073,"type":"personal","transaction":"regular"},
           {"name":"madhan","gpaynum":9940235467,"type":"personal","transaction":"rare"},
           {"name":"madhumitha","gpaynum":7358602342,"type":"personal","transaction":"regular"},
           {"name":"madhuri","gpaynum":9500771102,"type":"personal","transaction":"regular"},
           {"name":"maha","gpaynum":9092042867,"type":"personal","transaction":"regular"},
           {"name":"parveen","gpaynum":8838105667,"type":"personal","transaction":"regular"},
           {"name":"pavithra","gpaynum":6369772429,"type":"personal","transaction":"regular"},
           {"name":"philip","gpaynum":9790830981,"type":"personal","transaction":"regular"},
           {"name":"pinky","gpaynum":9489300189,"type":"personal","transaction":"regular"},
           {"name":"rohini","gpaynum":6380874698,"type":"personal","transaction":"rare"},
           {"name":"sabitha","gpaynum":9361447138,"type":"personal","transaction":"regular"},
           {"name":"sagarika","gpaynum":7358701090,"type":"personal","transaction":"regular"},
           {"name":"sameera","gpaynum":6382718022,"type":"personal","transaction":"regular"},
           {"name":"sandhiya","gpaynum":6383138140,"type":"personal","transaction":"rare"},
           {"name":"sangeetha","gpaynum":7904104077,"type":"personal","transaction":"regular"},]


for i in googlepay:                                                                                                                      #LOOPING
    for j,k in i.items():                                                                                                                #KEY VALUES LOOPING
        print(f"{j}:{k}")
    
