def check_progress(i, n):
  if i % (n//100) == 0:
    print("..." + str(i // (n//100)) + "%", end="\r")