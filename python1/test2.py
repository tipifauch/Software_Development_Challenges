import fileinput

file=fileinput.input()
print file.readline()


def readline(self):
        try:
            line = self._buffer[self._bufindex]
        except IndexError:
            pass
        else:
            self._bufindex += 1
            self._lineno += 1
            self._filelineno += 1
            return line
        if not self._file:
            if not self._files:
                return ""
            self._filename = self._files[0]
            self._files = self._files[1:]
            self._filelineno = 0
            self._file = None
            self._isstdin = 0
            self._backupfilename = 0
            if self._filename == '-':
                self._filename = '<stdin>'
                self._file = sys.stdin
                self._isstdin = 1
            else:
                if self._inplace:
                    self._backupfilename = (
                        self._filename + (self._backup or os.extsep+"bak"))
                    try: os.unlink(self._backupfilename)
                    except os.error: pass
                    # The next few lines may raise IOError
                    os.rename(self._filename, self._backupfilename)
                    self._file = open(self._backupfilename, "r")
                    try:
                        perm = os.fstat(self._file.fileno())[stat.ST_MODE]
                    except:
                        self._output = open(self._filename, "w")
                    else:
                        fd = os.open(self._filename,
                                     os.O_CREAT | os.O_WRONLY | os.O_TRUNC,
                                     perm)
                        self._output = os.fdopen(fd, "w")
                        try:
                            os.chmod(self._filename, perm)
                        except:
                            pass
                    self._savestdout = sys.stdout
                    sys.stdout = self._output
                else:
                    # This may raise IOError
                    self._file = open(self._filename, "r")
        self._buffer = self._file.readlines(self._bufsize)
        self._bufindex = 0
        if not self._buffer:
            self.nextfile()
        # Recursive call
        return self.readline()
