# assignments
I made different branches for each assignment.
<div class="container form-group m-5">
  <form>
    <div class="row my-2">
      <div class="col-3">
        <div class="placeholder">
          <label for="fn">First Name<span>*</span></label>
        </div>
        <input
          (click)="onClick($event)"
          (blur)="onBlur($event)"
          class="form-control"
          required
          type="text"
          id="fn"
        />
      </div>
      <div class="col-3">
        <div class="placeholder">
          <label for="ln">Last Name<span>*</span></label>
        </div>
        <input
          (click)="onClick($event)"
          (blur)="onBlur($event)"
          id="ln"
          required
          class="form-control required"
          type="text"
        />
      </div>
      <div class="col-3">
        <div class="placeholder">
          <label for="npi">NPI<span>*</span></label>
        </div>
        <input
          (click)="onClick($event)"
          (blur)="onBlur($event)"
          id="npi"
          required
          class="form-control"
          type="text"
        />
      </div>
      <div class="col-3">
        <div class="placeholder">
          <label for="tin">TIN</label>
        </div>
        <input
          (click)="onClick($event)"
          (blur)="onBlur($event)"
          id="tin"
          class="form-control"
          type="text"
        />
      </div>
    </div>
    <div class="row my-2">
      <div class="col-9">
        <div class="placeholder">
          <label for="address">Address<span>*</span></label>
        </div>
        <input
          (click)="onClick($event)"
          (blur)="onBlur($event)"
          id="address"
          class="form-control"
          type="text"
          required
        />
      </div>
      <div class="col-3">
        <div class="placeholder">
          <label for="ph">Phone Number<span>*</span></label>
        </div>
        <input
          (click)="onClick($event)"
          (blur)="onBlur($event)"
          id="ph"
          required
          class="form-control"
          type="text"
        />
      </div>
    </div>
    <div class="row my-2">
      <div class="col-3">
        <div class="placeholder">
          <label for="fx">Fax Number<span>*</span></label>
        </div>
        <input
          (click)="onClick($event)"
          (blur)="onBlur($event)"
          id="fx"
          class="form-control"
          type="text"
          required
        />
      </div>
      <div class="col-3">
        <div class="placeholder">
          <label for="email">Email Address<span>*</span></label>
        </div>
        <input
          (click)="onClick($event)"
          (blur)="onBlur($event)"
          id="email"
          class="form-control"
          type="text"
        />
      </div>
    </div>
  </form>
</div>
