function updateMotion(self) {
    let entity = self.attributes;
    let entities = document.getElementsByTagName("circle");
    // Identifying border colision
    let lb = (float(entity.cx.value)-float(entity.r.value) <= 0) ? -1 : 1;
    let rb = (float(entity.cx.value)+float(entity.r.value) >= 100) ? -1 : 1;
    let tb = (float(entity.cy.value)-float(entity.r.value) <= 0) ? -1 : 1;
    let bb = (float(entity.cy.value)+float(entity.r.value) >= 100) ? -1 : 1;
    // Reverting the vector direction where border colision happens
    self.setAttribute("vi", `${float(entity.vi.value) * lb*rb}%`);
    self.setAttribute("vj", `${float(entity.vj.value) * tb*bb}%`);
    // Get the total sum of vectors that mus be applied for each entity
    let total_sum_x = 0;
    let total_sum_y = 0;
    for (var i=0; i<entities.length; i++) {
        _ent = entities[i].attributes;
        if (float(entity.id.value) != float(_ent.id.value)) {
            total_sum_x += (Math.sqrt((float(entity.cx.value)-float(_ent.cx.value))**2+(float(entity.cy.value)-float(_ent.cy.value))**2) <= float(entity.r.value)+float(_ent.r.value) ) ? (float(_ent.vi.value)-float(entity.vi.value)) : 0
            total_sum_y += (Math.sqrt((float(entity.cx.value)-float(_ent.cx.value))**2+(float(entity.cy.value)-float(_ent.cy.value))**2) <= float(entity.r.value)+float(_ent.r.value) ) ? (float(_ent.vj.value)-float(entity.vj.value)) : 0
        }
    }
    
    self.setAttribute("cx", `${float(entity.cx.value) + total_sum_x + float(entity.vi.value)}%`)
    self.setAttribute("cy", `${float(entity.cy.value) + total_sum_y + float(entity.vj.value)}%`)
}
function float(str) {
    return Number(str.slice(0, -1))
}

function startProcessing(self) {
    let entities = self.getElementsByTagName("circle")
    for (let entity of entities) {
        updateMotion(entity)
    }
}
window.startProcessing = startProcessing
window.float = float
window.updateMotion = updateMotion