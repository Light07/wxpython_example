#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

import wx

class MainWindow(wx.Frame):

    p_file = os.path.dirname(__file__)
    icon_folder = os.path.join(p_file, 'icons')

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.dir_name = ''
        self.file_name = ''
        self.current = False
        self.CreateStatusBar()

        # setting up the menu
        # file_menu = wx.Menu()

        # menu_new = file_menu.Append(wx.ID_NEW, "N&ew", "New a file")
        # menu_open = file_menu.Append(wx.ID_OPEN, "&Open", "Open a file")
        # menu_save = file_menu.Append(wx.ID_SAVE, "&Save", "Save")
        # menu_save_as = file_menu.Append(wx.ID_SAVEAS, "&Save As", "Save as a file")

        # # Sub Menu
        # imp = wx.Menu()
        # imp.Append(wx.ID_ANY, 'Import new feed list...')
        # imp.Append(wx.ID_ANY, 'Import bookmarks...')
        # imp.Append(wx.ID_ANY, 'Import email...')
        #
        # file_menu.AppendMenu(wx.ID_ANY, '&Import', imp)


        file_menu = wx.Menu()
        f_new = wx.MenuItem(file_menu, wx.ID_NEW, '&New\t Ctrl+N')
        f_new.SetBitmap(wx.Bitmap(os.path.join(self.icon_folder, 'new.png')))
        menu_new = file_menu.AppendItem(f_new)

        f_open = wx.MenuItem(file_menu, wx.ID_OPEN, '&Open\t Ctrl+O')
        f_open.SetBitmap(wx.Bitmap(os.path.join(self.icon_folder, 'open.png')))
        menu_open = file_menu.AppendItem(f_open)

        f_save = wx.MenuItem(file_menu, wx.ID_SAVE, '&Save\t Ctrl+S')
        f_save.SetBitmap(wx.Bitmap(os.path.join(self.icon_folder, 'save.png')))
        menu_save = file_menu.AppendItem(f_save)

        f_save_as = wx.MenuItem(file_menu, wx.ID_SAVEAS, '&SaveAs')
        f_save_as.SetBitmap(wx.Bitmap(os.path.join(self.icon_folder, 'saveas.png')))
        menu_save_as = file_menu.AppendItem(f_save_as)

        file_menu.AppendSeparator()
        # Add a pic and shor cut.
        qmi = wx.MenuItem(file_menu, wx.ID_EXIT, '&Exit\t Ctrl+Q')
        qmi.SetBitmap(wx.Bitmap(os.path.join(self.icon_folder, 'exit.png')))
        menu_Exit = file_menu.AppendItem(qmi)

        help_menu = wx.Menu()
        m_help = wx.MenuItem(help_menu, wx.ID_ABOUT, '&About\t Ctrl+A' )
        m_help.SetBitmap(wx.Bitmap(os.path.join(self.icon_folder, 'about.png')))
        menu_help = help_menu.AppendItem(m_help)

        # createing the menu bar
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, '&File')
        menu_bar.Append(help_menu, '&Help')
        self.SetMenuBar(menu_bar)

        #set events
        self.Bind(wx.EVT_MENU, self.OnAbout, menu_help)
        self.Bind(wx.EVT_MENU, self.OnExit, menu_Exit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menu_open)
        self.Bind(wx.EVT_MENU, self.OnSave, menu_save)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menu_save_as)
        self.Bind(wx.EVT_MENU, self.OnNew, menu_new)

        self.Center()
        self.Show()

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "Version 1.0", "About", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        dlg = wx.MessageDialog(self, "Are you sure you want to exit?", "Exit")
        if dlg.ShowModal()== wx.ID_OK:
            dlg.Destroy()
            self.Close(True)
        else:
            dlg.Destroy()

    def OnNew(self, e):
        self.control.Clear()
        self.file_name = ''
        self.dir_name = ''

    def OnOpen(self, e):
        dlg = wx.FileDialog(self, "Choose a file", self.dir_name, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.file_name = dlg.GetFilename()
            self.dir_name = dlg.GetDirectory()
            f = open(os.path.join(self.dir_name, self.file_name), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnSave(self,e):
        if self.file_name:
            print "true"
            print self.dir_name
            print self.file_name
            self.SaveFile(e)
        else:
            self.OnSaveAs(e)

    def OnSaveAs(self, e):
        dialog = wx.FileDialog(self,message='Save as a file:',
                                defaultDir=self.dir_name,
                                defaultFile=self.file_name,
                                wildcard='*.*',style=wx.SAVE,
                                )
        if dialog.ShowModal() ==wx.ID_OK:
            (self.dir_name,self.file_name)	= os.path.split(dialog.GetPath())
            # self.SetTitle(dialog.GetPath()+'- Notepad Easy ')
            self.current =True
            dialog.Destroy()
            self.SaveFile(e)
        else:
            dialog.Destroy()

    def SaveFile(self, e):
        textfile = open(os.path.join(self.dir_name,self.file_name),'w')
        textfile.write(self.control.GetValue())
        textfile.close()

if __name__ == "__main__":

    app = wx.App(False)
    frame = MainWindow(None, "iTesting")
    app.MainLoop()
