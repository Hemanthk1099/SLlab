def elements():
    periodictable={
    "H":"Hydrogen",
    "Ne":"Neon",
    "Cl":"Chlorine",
    "Al":"Aluminium",
    "C":"Carbon",
    "O":"Oxygen"
    }
    while True:
        print("1.Add 2.Search 3.Length 4.Display 5.Exit")
        ch=int(input("Enter choice:"))
        if ch==1:
            periodictable.update({str(input("Enter symbol:")):str(input("Enter element:"))})
        elif ch==2:
            sym=str(input("Enter symbol:"))
            if sym in periodictable:
                print(periodictable[sym])
            else:
                print("Element not found")
        elif ch==3:
            print("No. of elements:",len(periodictable))
        elif ch==4:
            print(periodictable)
        elif ch==5:
            exit()
        else:
            print("Invalid choice")
elements()
