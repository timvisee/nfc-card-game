extends Node2D

@export var type: Global.MinerType = Global.MinerType.MINER1;
@export var color: Color = Color.WHITE;

@onready var sprite = $Sprite;

# Called when the node enters the scene tree for the first time.
func _ready():
	self.update_miner_type(self.type);
	self.sprite.modulate = self.color;


func update_miner_type(type: Global.MinerType):
	match type:
		Global.MinerType.MINER1:
			self.sprite.animation = "miner1";
		Global.MinerType.MINER2:
			self.sprite.animation = "miner2";
		Global.MinerType.MINER3:
			self.sprite.animation = "miner3";
		_:
			assert(false, "unknown miner type");


func destroy():
	if is_instance_valid(self):
		self.queue_free();
