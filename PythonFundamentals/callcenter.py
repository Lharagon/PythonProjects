class CallCenter(object):

    calls = []
    
    
    def __init__(self):
        self.queue_size = 0

    def Add(self,caller):
        self.calls.append(caller)
        self.queue_size += 1
        return self
    
    def Remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self
     
    def info(self):
        print "People on the queue: %s \n" % (myCallCenter.queue_size )
        for callers in range(len(self.calls)):
            print "Name: " + self.calls[callers].caller_name
            print "Phone: " + self.calls[callers].caller_phone + "\n"
        return self
    
    def Remove_By_Phone(self, phone):
        for callers in range(len(self.calls)):
            if self.calls[callers].caller_phone == phone:
                self.calls.pop(callers)
                self.queue_size -= 1
                break
    
    def Sort_By_Time(self):
        self.calls = sorted(self.calls, key=lambda caller: caller.time)
        return self
        
        
class Call(object):

    def __init__(self,caller_id,caller_name,caller_phone,time,reason):
        self.caller_id = caller_id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time = time
        self.reason = reason
        
        
        #myCallCenter.Add(self)

    def Display(self):
        print "id: %s" % (self.caller_id)
        print "Caller Name: %s" % (self.caller_name)
        print "Caller Phone: %s" % (self.caller_phone)
        print "Time of Call: %s" % (self.time)
        print "Reason For Call: %s" % (self.reason)

Steve = Call(1, "Steve","323-746-3902","3:20","Fell Can't get up")
John = Call(2, "John","323-463-0002","5:40","Nothing")
Bill = Call(3, "Bill","562-111-8888","3:16","Fearlessness")

myCallCenter = CallCenter()

myCallCenter.Add(Steve)
myCallCenter.Add(John)
myCallCenter.Add(Bill)
myCallCenter.info()
myCallCenter.Remove_By_Phone("323-463-0002")
myCallCenter.info()
myCallCenter.Sort_By_Time()
myCallCenter.info()

