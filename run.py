import writer
import filereader

def run():
    writer.write("data.txt", "new stuff in file\n")
    filereader.read("data.txt")

run()
