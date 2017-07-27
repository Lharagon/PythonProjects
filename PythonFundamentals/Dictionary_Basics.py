me = {
	"name": "Luis",
	"age": "89",
	"country": "The United States",
	"language": "Armenian"
}

def me_info(dict):
	print "My name is " + dict["name"]
	print "My age is " + str(dict["age"])
	print "My country of birth is " + dict["country"]
	print "My favorite language " + dict["language"]

me_info(me)