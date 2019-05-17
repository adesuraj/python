import re
space = re.compile("\s+")


fh = open("taa.txt")
fho = open("csv.txt","w")
pattern=","
while True:
        record = fh.readline(60)
        if not record:
                break
        print(record)

        values = space.split(record)
        fho.write('"'+",".join(values)+'\n')

fho.close()