extends Node


func _process(_delta):
	if Input.is_action_just_pressed("quit"):
		self.quit();
		return;
	if Input.is_action_just_pressed("toggle_fullscreen"):
		self.toggle_fullscreen();
		return;

func _notification(what):
	if what == NOTIFICATION_WM_CLOSE_REQUEST:
		self.quit();
		
		
func quit():
	self.get_tree().quit();


func toggle_fullscreen():
	if DisplayServer.window_get_mode() == DisplayServer.WINDOW_MODE_MAXIMIZED:
		DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_WINDOWED);
	else:
		DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_MAXIMIZED);
