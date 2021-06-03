from enum import Enum


class BackendRarity(Enum):
    Transcendent = 'EFortRarity::Transcendent'
    Legendary = 'EFortRarity::Legendary'
    Epic = 'EFortRarity::Epic'
    Rare = 'EFortRarity::Rare'
    Uncommon = 'EFortRarity::Uncommon'
    Common = 'EFortRarity::Common'


class BackendType(Enum):
    Backpack = 'AthenaBackpack'
    Wrap = 'AthenaItemWrap'
    Glider = 'AthenaGlider'
    Pickaxe = 'AthenaPickaxe'
    Outfit = 'AthenaCharacter'
    Pet = 'AthenaPet'
    Music_Pack = 'AthenaMusicPack'
    Loading_Screen = 'AthenaLoadingScreen'
    Emote = 'AthenaDance'
    Spray = 'AthenaSpray'
    Emoji = 'AthenaEmoji'
    Contrail = 'AthenaSkyDiveContrail'
    Pet_Carrier = 'AthenaPetCarrier'
    Toy = 'AthenaToy'
    Consumable_Emote = 'AthenaConsumableEmote'
    Battle_Bus = 'AthenaBattleBus'
    Reward_Event_Graph_Cosmetic = 'AthenaRewardEventGraphCosmetic'
    Victory_Pose = 'AthenaVictoryPose'
