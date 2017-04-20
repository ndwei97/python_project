with open('index.html') as fin, open('index_1.html','w') as fout:
    for line in fin:
        fout.write(line)
        if line == '        <div id="myDropdown" class="dropdown-content">\n':
           next_line = next(fin)
           if next_line == '          <a href="index.html">Home </a>\n':
              for i in range(4000):
                  fout.write('     <a href="index.html">My line </a>\n')
           fout.write(next_line)
