
try:
    a=int(input("Enter : "))

except Exception as e:
    print(e)

else:
    print("All done")

finally:
    print("Finially")