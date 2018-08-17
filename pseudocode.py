#versionnum = docopt(doc, '--version')
#self.assertEqual(versionnum['--version'], True)


#self.assertEqual(docstring['--version'], False)


# saved_stdout = sys.stdout
# try:
#     out = StringIO()
#     sys.stdout = out
#     docopt(doc, version='hi')
#     output = out.getvalue().strip()
#     self.assertEqual(output, "1.0.0")
# finally:
#     sys.stdout = saved_stdout
