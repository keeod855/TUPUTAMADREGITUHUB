const { Client, MessageEmbed } = require('discord.js')
const client = new Client()
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database("./database/perms.sqlite");
var prefix = "."

client.on("message", async (message) => {

const args = message.content.substring(prefix.length).split(" ")

if (message.content.startsWith(`${prefix}dtp`)) {
   var id = ["452272278776971264", "814506142868570163"]
   if(!id.some(id => message.author.id == id)) return message.channel.send(new MessageEmbed().setDescription('Solo ED y Owner').setColor('BLACK'))


        let userm = message.mentions.users.first() || client.users.cache.get(args[1]);

        if (!args[1]) return message.channel.send(new MessageEmbed().setDescription('Ingresa una ID o menciona un usuario').setColor('BLACK'))


db.run('INSERT INTO perms (id) values (?)',
            [userm.id]);
 message.channel.send(new MessageEmbed().setDescription("<@"+userm.id+"> fue registrado."));

}


})

client.on('ready', async ()  => {
  console.log('listo')
})

client.login("ODM1Mjg3OTIwNjMzMDUzMjI1.YINQfw.bbYs2BeWSOEmT7chg1NNhjJfaL4")
