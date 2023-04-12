#!/usr/bin/env python3
import subprocess

def test(filein, ID, eout, eerr):
    proc = subprocess.Popen(['./receiver', ID], cwd="receiver", stdin = open(filein), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if (stdout.decode() != eout or (eerr != (stderr.decode() != ""))):
        print("res:" + stdout.decode())
        print("expected: " + eout)
        print("err: " + stderr.decode())
        return False
    else:
        print("pass")
    return True

subprocess.Popen(["rm", "-rf", "receiver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["mkdir", "receiver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["unzip", "receiver.zip", "-d", "receiver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["chmod", "+x", "compile"], cwd="receiver", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["chmod", "+x", "receiver"], cwd="receiver", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
subprocess.Popen(["./compile"], cwd="receiver", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

test("input.txt", "12345", "ABCDEFGHJ\n", False)

subprocess.Popen(["rm", "-rf", "receiver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

