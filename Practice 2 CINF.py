{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b4dcd8a8-ee01-4f88-94f1-7c93ee0f12aa",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Options:\n",
      "1. Add a book to the inventory\n",
      "2. Remove a book from the inventory\n",
      "3. Display the inventory\n",
      "4. Quit the program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  1\n",
      "Enter the book title:  The Hunger Games\n",
      "Enter the author's name:  Suzanne Collins\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Hunger Games by Suzanne Collins added to the inventory.\n",
      "\n",
      "Options:\n",
      "1. Add a book to the inventory\n",
      "2. Remove a book from the inventory\n",
      "3. Display the inventory\n",
      "4. Quit the program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  1\n",
      "Enter the book title:  Divergent\n",
      "Enter the author's name:  Veronica Roth\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Divergent by Veronica Roth added to the inventory.\n",
      "\n",
      "Options:\n",
      "1. Add a book to the inventory\n",
      "2. Remove a book from the inventory\n",
      "3. Display the inventory\n",
      "4. Quit the program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current Inventory:\n",
      "The Hunger Games by Suzanne Collins\n",
      "Divergent by Veronica Roth\n",
      "\n",
      "Options:\n",
      "1. Add a book to the inventory\n",
      "2. Remove a book from the inventory\n",
      "3. Display the inventory\n",
      "4. Quit the program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  2\n",
      "Enter the title of the book to remove:  The Hunger Gams\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: The Hunger Gams not found in the inventory.\n",
      "\n",
      "Options:\n",
      "1. Add a book to the inventory\n",
      "2. Remove a book from the inventory\n",
      "3. Display the inventory\n",
      "4. Quit the program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  2\n",
      "Enter the title of the book to remove:  Divergent\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Divergent removed from the inventory.\n",
      "\n",
      "Options:\n",
      "1. Add a book to the inventory\n",
      "2. Remove a book from the inventory\n",
      "3. Display the inventory\n",
      "4. Quit the program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current Inventory:\n",
      "The Hunger Games by Suzanne Collins\n",
      "\n",
      "Options:\n",
      "1. Add a book to the inventory\n",
      "2. Remove a book from the inventory\n",
      "3. Display the inventory\n",
      "4. Quit the program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Goodbye! Come back soon!\n"
     ]
    }
   ],
   "source": [
    "book_inventory = {}\n",
    "\n",
    "def add_book():\n",
    "    title = input(\"Enter the book title: \")\n",
    "    author = input(\"Enter the author's name: \")\n",
    "    book_inventory[title] = author\n",
    "    print(f\"{title} by {author} added to the inventory.\")\n",
    "\n",
    "def remove_book():\n",
    "    title = input(\"Enter the title of the book to remove: \")\n",
    "    if title in book_inventory:\n",
    "        del book_inventory[title]\n",
    "        print(f\"{title} removed from the inventory.\")\n",
    "    else:\n",
    "        print(f\"Error: {title} not found in the inventory.\")\n",
    "\n",
    "def display_inventory():\n",
    "    if not book_inventory:\n",
    "        print(\"The inventory is empty.\")\n",
    "    else:\n",
    "        print(\"Current Inventory:\")\n",
    "        for title, author in book_inventory.items():\n",
    "            print(f\"{title} by {author}\")\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        print(\"\\nOptions:\")\n",
    "        print(\"1. Add a book to the inventory\")\n",
    "        print(\"2. Remove a book from the inventory\")\n",
    "        print(\"3. Display the inventory\")\n",
    "        print(\"4. Quit the program\")\n",
    "\n",
    "        choice = input(\"Enter your choice (1-4): \")\n",
    "\n",
    "        if choice == '1':\n",
    "            add_book()\n",
    "        elif choice == '2':\n",
    "            remove_book()\n",
    "        elif choice == '3':\n",
    "            display_inventory()\n",
    "        elif choice == '4':\n",
    "            print(\"Goodbye! Come back soon!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Error: Invalid choice. Please enter a number between 1 and 4.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82e297f3-0b20-4490-93cb-b1a6070fd1df",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
