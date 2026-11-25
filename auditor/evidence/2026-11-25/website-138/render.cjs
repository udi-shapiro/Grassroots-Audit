const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const page = fs.readFileSync('glp/servers/peoplesweb/web/index.html', 'utf8');
const start = page.indexOf('function schemaHtml(s, open)');
const end = page.indexOf('/* ---------- papers',start);
assert.ok(start >= 0 && end > start);
const context = {
  C: {Booking:{name:'Booking'}, 'Tennis-Courts':{name:'Tennis Courts'}},
  book: JSON.parse(fs.readFileSync('book.json','utf8'))
};
const helpers = page.split('\n').filter(line => /^const (esc|NM) = /.test(line)).join('\n');
const html = vm.runInNewContext(helpers+'\n'+page.slice(start,end)+'\nschemaHtml(book, true)',context);
assert.ok(html.includes('<span>Book</span><span class="fr">Booking + Tennis Courts</span>'));
assert.ok(html.includes('needs the will of Alice and Carol'));
console.log('Extracted renderer: Book displays both origins and both consent roles.');
