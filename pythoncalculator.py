#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# calculator.py

def main():
    while True:
        print("\n=== Team Calculator ===")
        print("1. Basic Operations")
        print("2. Scientific Operations")
        print("3. Fun Math")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Basic operations selected.")
        elif choice == '2':
            print("Scientific operations selected.")
        elif choice == '3':
            print("Fun math selected.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


# In[ ]:




