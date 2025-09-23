import { Component, OnInit } from '@angular/core';
import { ApiService } from './services/api.service';


@Component({
selector: 'app-root',
templateUrl: './app.component.html'
})
export class AppComponent implements OnInit {
items: any[] = [];
newItem = '';


constructor(private apiService: ApiService) {}


ngOnInit(): void {
this.loadItems();
}


loadItems() {
this.apiService.getItems().subscribe(data => this.items = data);
}


addItem() {
if (!this.newItem) return;
this.apiService.createItem({ name: this.newItem, description: 'Demo description' })
.subscribe(() => {
this.newItem = '';
this.loadItems();
});
}
}
