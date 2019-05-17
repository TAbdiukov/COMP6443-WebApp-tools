alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
with open("bl.txt", "w") as f:
	for i in alpha:
		for j in alpha:
			for k in alpha:
				for l in alpha:
					for m in alpha:
						for n in alpha:
							f.write(i)
							f.write(i)
							f.write(i)
							f.write(i)
							f.write(i)
							f.write(i)
							f.write("\n")
