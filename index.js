const { AoiClient } = require("aoi.js");
const { Database } = require("aoi.sqlite");
const { token } = require(`./config.json`);

// 10.5.24 npm i github:aoijs/aoi.js#v6

const bot = new AoiClient({
  token: token,
  prefix: "#",
  intents: [
    "MessageContent",
    "Guilds",
    "GuildMembers",
    "GuildPresences",
    "GuildMessages",
    "GuildVoiceStates",
    "GuildIntegrations",
    "GuildWebhooks",
    "GuildInvites",
    // "GuildVoiceDiscovery", // no work?
    "GuildEmojisAndStickers",
    "GuildMessageReactions",
    // "GuildChannelMessages", // no work?
    // "GuildTyping", // no work?
    "GuildMessageTyping",
    "GuildScheduledEvents",
    "GuildVoiceStates",
    "GuildIntegrations",
    "GuildWebhooks",
    "GuildInvites",
    "DirectMessages",
    "DirectMessageReactions",
    "DirectMessageTyping",
    "GuildMembers",
    "GuildPresences",
    "GuildVoiceStates",
    "GuildBans",
  ],
  events: [
    "onMessage",
    "onMessageDelete",
    "onMessageUpdate",
    "onMessageDeleteBulk",
    "onReactionAdd",
    "onReactionRemove",
    "onReactionRemoveAll",
    "onInviteCreate",
    "onInviteDelete",
    "onGuildJoin",
    "onGuildLeave",
    "onGuildUpdate",
    "onGuildUnavailable",
    "onRoleCreate",
    "onRoleUpdate",
    "onRoleDelete",
    "onChannelCreate",
    "onChannelUpdate",
    "onChannelDelete",
    "onChannelPinsUpdate",
    "onStageInstanceCreate",
    "onStageInstanceUpdate",
    "onStageInstanceDelete",
    "onThreadCreate",
    "onThreadUpdate",
    "onThreadDelete",
    "onThreadListSync",
    "onThreadMemberUpdate",
    "onThreadMembersUpdate",
    "onEmojiCreate",
    "onEmojiUpdate",
    "onEmojiDelete",
    "onStickerCreate",
    "onStickerUpdate",
    "onStickerDelete",
    "onBanAdd",
    "onBanRemove",
    "onVoiceStateUpdate",
    "onWebhooksUpdate",
    "onJoin",
    "onLeave",
    "onMemberUpdate",
    "onMemberAvailable",
    "onMembersChunk",
    "onPresenceUpdate",
    "onTypingStart",
    "onUserUpdate",
    "onInteractionCreate",
    "onFunctionError",
    "onApplicationCommandPermissionsUpdate",
    "onVariableCreate",
    "onVariableUpdate",
    "onVariableDelete",
    // "onShardDisconnect", // no work?
    // "onShardError", // no work?
    // "onShardReady", // no work?
    // "onShardReconnecting", // no work?
    // "onShardResume" // no work?
  ],
  database: {
    type: "aoi.db",
    db: require("@akarui/aoi.db"),
    path: "./Database/",
    tables: ["main", "Bank"],
  },
  guildOnly: false,
  respondToBots: true,
  // aoiAutoUpdate: true,
  respondOnEdit: {
    commands: true,
    time: 1000000000000,
    nonPrefixed: false,
  },
  disableAoiDB: true, // This is important, you can't use both at once.
});

new Database(bot, {
  location: "./Database/database.db",
  tables: ["main", "Bank"],
  logging: false,
});

bot.loadCommands("./Commands/", true);

bot.command({
  name: "test",
  code: `
    $math[$getGlobalUserVar[Money;$authorID;Bank]+(2*$message)]
    $getGlobalUserVar[Money;$authorID;Bank]
    `,
});

bot.variables(
  {
    DisboardBumpChannel: "",
  },
  "main",
  {
    Money: 0,
  },
  "Bank"
);

bot.status({
  status: "online", // options: online, idle, dnd, invisible
  type: "competing", // options: WATCHING, PLAYING, LISTENING, COMPETING, STREAMING (if you choose streaming, you can also add the url: '' property)
  name: "On $guildCount server(s), and made by LightslicerGP#2125, prefix is #", // Whatever text you want, you can use $guildCount and $allMembersCount too.
  time: 10, // If you want multiple statuses add the time property for how long each status will be until it switches.
});

bot.status({
  status: "online",
  type: "streaming",
  name: "AOIJS VERSION",
  time: 5,
  url: "https://aoi.js.org/guides/",
});
