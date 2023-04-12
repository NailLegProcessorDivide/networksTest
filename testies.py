#!/usr/bin/env python3
import subprocess

testn = 0

def test(filein, ID, eout, eerr):
    global testn
    testn += 1
    proc = subprocess.Popen(['./receiver', ID], cwd="receiver", stdin = open(filein), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if (stdout.decode() != eout or (eerr != (stderr.decode() != ""))):
        print("test: ", testn)
        print("res:" + stdout.decode())
        print("expected: " + eout)
        print("err: " + stderr.decode())
        return False
    else:
        print("pass ", testn)
    return True

subprocess.Popen(["rm", "-rf", "receiver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["mkdir", "receiver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["unzip", "receiver.zip", "-d", "receiver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["chmod", "+x", "compile"], cwd="receiver", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["chmod", "+x", "receiver"], cwd="receiver", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["./compile"], cwd="receiver", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

test("input.txt", "12345", "ABCDEFGHI\n", False)
test("input.txt", "12344", "", True)
test("input2.txt", "12345", "", True)
test("input3.txt", "12345", "", True)
test("input4.txt", "12345", "A\n", False)
test("input5.txt", "12345", "ABCDEFGHI\n", False)
test("input6.txt", "123456", "", True)
test("input7.txt", "1", "ABCDEFGHI\n", False)
test("input8.txt", "1", "ABCDEFGHI\n", False)
test("input9.txt", "12345", "ABCDEFGHI\n", False)
test("input10.txt", "12345", "", True)
test("input11.txt", "12345", "", True)
test("input12.txt", "12345", "In The Beginning Light It Was Good Then God Said\n", False)
test("input13.txt", "-1", "", True)
test("input14.txt", "65536", "", True)
test("input15.txt", "12345", "ABCDE\n", False)

subprocess.Popen(["rm", "-rf", "receiver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

