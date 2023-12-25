


def cube():
    powers = 0
    with open("2/input.txt", "r") as f:
        lines = f.readlines()
        
        for l,line in enumerate(lines):
            rgb = [0,0,0]
            digit = ""
            
            for i,val in enumerate(line):
                if val.isdigit():
                    digit += str(val)
                    
                elif val == " " or val == ",":
                    continue
                
                elif line[i:].startswith("red"):
                    rgb[0] = max(rgb[0],int(digit))
                    digit=""
                    
                elif line[i:].startswith("blue"):
                    rgb[2] = max(rgb[2],int(digit))
                    digit=""
                    
                elif line[i:].startswith("green"):
                    rgb[1] = max(rgb[1],int(digit))
                    digit=""
            
            power = rgb[0] * rgb[1] * rgb[2]
            powers += power
            
    print(powers)
            


if __name__ == "__main__":
    cube()
# end main