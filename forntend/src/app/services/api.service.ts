import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({ providedIn: 'root' })
export class ApiService {
private baseUrl = 'https://<API_GATEWAY_HOST>/prod'; // replace with actual API


constructor(private http: HttpClient) {}


getItems(): Observable<any> {
return this.http.get(`${this.baseUrl}/items`);
}


createItem(payload: any): Observable<any> {
return this.http.post(`${this.baseUrl}/items`, payload);
}
}
