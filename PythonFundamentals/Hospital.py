class Hospital(object):

    patients = []

    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity

    def Admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Sorry, the hospital is FULL, you can't be admitted"
        else:	
            self.patients.append(patient);
            print "Welcome to the hospital, hope you enjoy your stay."

    def Discharge(self,patient_id):
        for person in range(len(self.patients)):
            if self.patients[person].id_number == patient_id:
                self.patients[person].bed_number = None;
                self.patients.pop(person)
                break

class Patient(object):

    def __init__(self,id_number,name,allergies,bed_number = None):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

    def show(self):
        print "%s %s %s" % (self.name, self.bed_number, self.id_number)
        
County = Hospital("County Hospital", 2)        

Chad = Patient(12,"Chad Chadson",['penuts','air','water'],13)
Roger = Patient(13, "Roger Rogerson", ['nothing'], 3)
Phil = Patient(15, "Phil Rogerson", ['nothing'], 4)


County.Admit(Chad)
County.Admit(Roger)
County.Admit(Phil)
Roger.show()
County.Discharge(13)
County.Admit(Phil)
Roger.show()