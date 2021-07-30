# Folder Copy
 Command line tool (mostly) to automatically copy folders to a destination for easy backing up to an online service or elsewhere.
 
### **THIS SOFTWARE IS GARBAGE AND I NO LONGER RECOMMEND USING IT. I HAVE NO PLANS OF MODIFYING OR IMPROVING IT! IF YOU WANT A BETTER TOOL FOR BACKING UP FOLDERS _AND_ FILES, CHECK OUT [GBP](https://github.com/ellman12/Graphical-Backup-Program).**

Something I often do is copying several "super important" folders to an external location like the cloud (in addition to a full PC backup). Things like video game save files, code, etc. I like to have extra backups of super important stuff like this. So instead of having to go hunting for all of those folders every time I want to back them up, I made this little script to automate the process. In my Run.ahk [AutoHotkey](https://github.com/ellman12/AutoHotkey) script, I have a command (just `fc`) that will clear the fc folder automatically if I want before running the actual fc Python script. I couldn't figure out how to do this with Python and plus I thought it would just be better to do that there. This is nice because I won't have tons of wasted space from old backups I no longer need.

In the `AppData/Roaming/fc` folder, there are 2 files fc requires. These 2 files will have to be created by you (maybe I should make the script do this automatically when running for the first time? 🤔). First file is `fc.conf`. So far this only has one line and thus one purpose. The first line should be exactly like this **with** a space at the end: `Default Copy Location: `. After the space, put where you want the stuff to be backed up by default (if you don't tell it where to copy stuff). E.g., `Default Copy Location: C:\Users\Elliott\Videos\fc`. This should work perfectly, as long as there is a space after the `:`.

The second file is `dirs.txt`, also in the same folder as `fc.conf`. This is a newline-delimited list of all the folders (and files? Haven't tested with single files) that the script will back up. For example:
```
C:\Users\Elliott\Pictures\Camera Roll
C:\Users\Elliott\Pictures\Dank Memes
C:\Users\Elliott\Documents\Important Documents
etc.
```
What follows is a table of all the commands, and what they do.
| Cmd Line Arg 1                | Cmd Line Arg 2        | What It Does                                                                                               |
|-------------------------------|-----------------------|------------------------------------------------------------------------------------------------------------|
| N/A                           | N/A                   | Copies folder to default dir specified in fc.conf                                                          |
| Help                          | N/A                   | Displays all the fc commands                                                                               |
| add                           | a directory           | Automatically adds a directory to `dirs.txt`                                                               |
| rm                            | a directory           | Automatically removes a directory from `dirs.txt`                                                          |
| ls                            | N/A                   | List all the directories in `dirs.txt`                                                                     |
| clr                           | N/A                   | Clears the contents of the `dirs.txt` file. Careful with this one!                                         |
| cp                            | Optional: a directory | If a directory specified, copy things in `dirs.txt` to there. If just `cp` arg given, copy to default dir. |
