from difflib import SequenceMatcher

with open("demoFile1.txt") as fileOne, open("demoFile2.txt") as fileTwo:
    data_file1 = fileOne.read()
    data_file2 = fileTwo.read()

    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f"The Plagieism content is {matches * 100:.2f}% ")